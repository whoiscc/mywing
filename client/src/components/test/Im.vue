<template>
  <div>
    <ul>
      <li v-for="recv in receivedList">{{ recv.id }}: {{ recv.message }}</li>
    </ul>
    Send to: <input type="text" v-model="receiver">
    Message: <input type="text" v-model="message">
    <button @click="submit" :style="inError ? {display: 'none'} : {}">Submit</button>
    <div :style="{color: inError ? 'red' : 'black'}">{{ status }}</div>
  </div>
</template>

<script>

import Im from '../../../lib/im'

export default {
  methods: {
    submit() {
      // console.log(this.angel);
      console.log('submitting...');
      this.im.send(this.message, {id: this.receiver});
    }
  },
  data() {
    return {
      receiver: '',
      message: '',
      status: '',
      inError: false,
      receivedList: [],
      im: null,
    }
  },
  props: ['angel'],
  created() {
    if (this.angel === null) {
      this.status = 'You need to login first',
      this.inError = true;
      return;
    }
    this.im = new Im(this.angel, message => {console.log('get it!'); this.receivedList.push(message)});
    this.im.start();
  },
  destroyed() {
    this.im && this.im.stop();
  },
}

</script>
