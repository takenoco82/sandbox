<template>
    <div>
        {{ msg }}
        <form>
            <button v-on:click="addTask()">Add Task</button>
            <button v-on:click="deleteTasks()">Delete Finished Tasks</button>
            <p>input: <input type="text" v-model="newTask"></p>
            <p>task: {{ newTask }}</p>
        </form>
        <div class="task-list">
            <ul>
                <li v-for="task in tasks" v-bind:key="task.id"><label class="task-list__item"><input type="checkbox" v-model="task.done"><button>Edit</button>{{ task.text }}</label></li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
  name: "tasklist",
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      tasks: [
        { id: 1, text: "vue-router", done: false },
        { id: 2, text: "vuex", done: false },
        { id: 3, text: "vue-loader", done: false },
        { id: 4, text: "awesome-vue", done: true }
      ],
      newTask: "test"
    };
  },
  methods: {
    addTask: function(event) {
      let text = this.newTask && this.newTask.trim();
      if (!text) {
        return;
      }
      this.tasks.push({
        id: this.tasks.length + 1,
        text: text,
        done: false
      });
    },
    deleteTasks: function(event) {
      for (let i = this.tasks.length - 1; i >= 0; i--) {
        const task = this.tasks[i];
        if (task.done) {
          console.log(task.text);
          this.tasks.splice(i, 1);
        }
      }
    }
  }
};
</script>

<style scoped>
.task-list ul li {
  list-style-type: none;
}
</style>
