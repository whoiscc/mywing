//

import IMService from './im-internal/im';

class Im {
  constructor(angel, onReceive) {
    this.token = angel.imToken;
    this.id = angel.id;
    this.onReceive = onReceive;
    this.active = false;
    this.localId = 0;
    this.im = null;
  }

  start() {
    const this_ = this;
    const observer = {
      handlePeerMessage: function (msg) {
        console.log(
          "msg sender:", msg.sender, " receiver:", msg.receiver,
          " content:", msg.content, " timestamp:", msg.timestamp
        );
        this_.onReceive({id: msg.sender, message: msg.content});
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
        } else if (state == IMService.STATE_CONNECTING) {
         console.log("im connecting");
        } else if (state == IMService.STATE_CONNECTFAIL) {
         console.log("im connect fail");
        } else if (state == IMService.STATE_UNCONNECTED) {
         console.log("im unconnected");
        }
      },
      onReset: function() {
        console.log("reset");
      }
    };

    this.im = new IMService();
    this.im.observer = observer;
    this.im.accessToken = this.token;
    this.im.start();

    this.active = true;
  }

  stop() {
    this.im.stop();
    this.active = false;
  }

  send(message, receiver) {
    if (!this.active) {
      throw new Error('Im instance is not active');
    }
    const msg = {
      sender: this.id,
      receiver: receiver.id,
      content: message,
      msgLocalID: this.localId,
    };
    this.localId += 1;
    this.im.sendPeerMessage(msg);
  }
}

export default Im;
