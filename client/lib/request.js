//

import axios from 'axios'

let base = '';

function requestFs() {
  return new Promise((resolve, reject) => {
    window.requestFileSystem(LocalFileSystem.PERSISTENT, 0, function (fs) {
      console.log('file system open: ' + fs.name);
      resolve(fs);
    }, reject);
  });
}

function storeToken(token) {
  return requestFs().then(fs => {
    return new Promise((resolve, reject) => {
      fs.root.getFile("token.txt", { create: true, exclusive: false }, function (fileEntry) {

          console.log("fileEntry is file?" + fileEntry.isFile.toString());
          // fileEntry.name == 'someFile.txt'
          // fileEntry.fullPath == '/someFile.txt'
          writeFile(fileEntry, new Blob([token], { type: 'text/plain' }))
            .then(resolve).catch(reject);

      }, reject);
    });
  });
}

function readToken() {
  return requestFs().then(fs => {
    return new Promise((resolve, reject) => {
      fs.root.getFile('token.txt', {}, entry => {
        readFile(entry).then(resolve).catch(reject);
      }, err => resolve(null));
    });
  });
}

function writeFile(fileEntry, dataObj) {
  return new Promise((resolve, reject) => {
    // Create a FileWriter object for our FileEntry (log.txt).
    fileEntry.createWriter(function (fileWriter) {

      fileWriter.onwriteend = function() {
        console.log("Successful file write...");
        resolve();
      };

      fileWriter.onerror = function (e) {
        console.log("Failed file write: " + e.toString());
        reject(e);
      };

      fileWriter.write(dataObj);
    });
  });
}

function readFile(fileEntry) {
  return new Promise((resolve, reject) => {
    fileEntry.file(function (file) {
      var reader = new FileReader();

      reader.onloadend = function() {
          console.log("Successful file read: " + this.result);
          resolve(this.result);
      };

      reader.readAsText(file);

    }, reject);
  });
}

class NotLoggedInError extends Error {
  constructor() {
    super('not logged in');
  }
}

function get(url, payload) {
  console.log('GET', base, url);
  return readToken().then(token => {
    if (!token) {
      throw new NotLoggedInError();
    }
    return axios.get(base + url + packGetPayload({...payload, token}));
  })
}

function post(url, payload) {
  console.log('POST', base, url);
  return readToken().then(token => {
    if (!token) {
      throw new NotLoggedInError();
    }
    return axios.post(base + url, {...payload, token});
  })
}

function packGetPayload(payload) {
  return '?data=' + JSON.stringify(payload);
}

function login(ticket) {
  return axios.post(base + '/angel/login', {ticket})
    .then(resp => {
      const token = resp.data.token;
      return storeToken(token);
    });
}

function set(conf) {
  base = conf.base || base;
}

export default {
  get,
  login,
  set,
};
