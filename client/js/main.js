const app = new Vue({
  el: "#app",
  data: {
    problemText: "",
    data: []
  },
  methods: {
    addData() {
      this.data = [
        ...this.data,
        { body: null, type: "", amount: "", unit: "", id: new Date().getTime() }
      ];
      console.log(JSON.parse(JSON.stringify(this.data)));
    },
    removeData(id) {
      this.data = this.data.filter(e => e.id != id);
    }
  }
});
