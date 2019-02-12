//

import axios from 'axios'

let base = '';

function requestTokenFile(arg) {
  return new Promise((resolve, reject) => {
    window.requestFileSystem(LocalFileSystem.PERSISTENT, 0, function (fs) {
      console.log('file system open: ' + fs.name);
      fs.root.getFile('token.txt', arg || {}, resolve, reject);
    }, reject);
  });
}

function storeToken(token) {
  return requestTokenFile({create: true, exclusive: false}).then(fileEntry => {
    console.log("fileEntry is file? " + fileEntry.isFile.toString());
    return writeFile(fileEntry, new Blob([token], { type: 'text/plain' }));
  });
}

function readToken() {
  return requestTokenFile().then(entry => {
    return readFile(entry);
  }).catch(err => null);
}

function removeToken() {
  return requestTokenFile().then(entry => {
    return new Promise((resolve, reject) => {
      console.log('removing: ', entry);
      entry.remove(resolve, reject);
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

class NetworkError extends Error {
  constructor(status) {
    super('network error: ' + status);
  }
}

class InternalError extends Error {
  constructor(message) {
    super('internal error: ' + message);
  }
}

class NotLoggedInError extends InternalError {
  constructor() {
    super('not logged in');
  }
}

function processResponse(resp) {
  if (resp.status != 200) {
    throw new NetworkError(resp.status);
  }
  if (resp.data.status != 0) {
    if (resp.data.status == 2) {
      throw new NotLoggedInError();
    } else {
      throw new InternalError(resp.data.message);
    }
  }
  return resp.data.data;
}

function get(url, payload) {
  console.log('GET', base, url);
  return readToken().then(token => {
    if (!token) {
      throw new NotLoggedInError();
    }
    return axios
      .get(base + url + packGetPayload({...payload, token}))
      .then(processResponse);
  })
}

function post(url, payload) {
  console.log('POST', base, url);
  return readToken().then(token => {
    if (!token) {
      throw new NotLoggedInError();
    }
    return axios
      .post(base + url, {...payload, token})
      .then(processResponse);
  })
}

function packGetPayload(payload) {
  return '?data=' + JSON.stringify(payload);
}

function login(ticket, debug = false) {
  return axios.post(base + '/angel/login' + (debug ? '~debug' : ''), {ticket})
    .then(processResponse)
    .then(data => {
      const token = data.token;
      return storeToken(token);
    });
}

function logout() {
  return post('/angel/logout').then(() => {
    return removeToken();
  });
}

function set(conf) {
  base = conf.base || base;
}

export default {
  get, post,
  login, logout,
  set,
};
