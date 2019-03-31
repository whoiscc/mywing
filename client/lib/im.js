//


let im = null;
function start(angel, onReceive) {
  if (im !== null) {
    throw new Error('you should stop old im instance before starting a new one');
  }

  return new Promise((resolve, reject) => {
    const observer = {
      handlePeerMessage: function (msg) {
        console.log(
          "msg sender:", msg.sender, " receiver:", msg.receiver,
          " content:", msg.content, " timestamp:", msg.timestamp
        );
        onReceive(msg);
      },
      handleMessageACK: function(msgLocalID, receiver) {
        console.log("message ack local id:", msgLocalID, " receiver:", receiver)
      },
      handleMessageFailure: function(msgLocalID, receiver) {
        console.log("message fail local id:", msgLocalID, " receiver:", receiver)
      },
      onConnectState: function(state) {
        if (state == IMService.STATE_CONNECTED) {
         console.log("im connected");
         resolve();
        } else if (state == IMService.STATE_CONNECTING) {
         console.log("im connecting");
        } else if (state == IMService.STATE_CONNECTFAIL) {
         console.log("im connect fail");
         reject();
        } else if (state == IMService.STATE_UNCONNECTED) {
         console.log("im unconnected");
        }
      },
      onReset: function() {
        console.log("reset");
      }
    };

    im = new IMService(observer);
    im.accessToken = angel.imToken;
    im.start();
  });
}


let localId = 0;
function send(angel, receiver, content) {
  msg = {sender: angel.imId, receiver: receiver.imId, content, msgLocalID: localId};
  localId += 1;
  im.sendPeerMessage(msg);
}

function stop() {
  im.stop();
  im = null;
}

export default {
  start, send, stop
};
