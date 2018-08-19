<template>
    <div>
        {{ msg }}
        <form>
            <button>Add Task</button>
            <button>Delete Finished Tasks</button>
            <p>input: <input type="text" v-model="newTask"></p>
            <p>task: {{ newTask }}</p>
        </form>
        <div class="task-list">
            <ul>
                <li v-for="todo in todos" v-bind:key="todo.id"><label class="task-list__item"><input type="checkbox"><button>Edit</button>{{ todo.text }}</label></li>
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
      todos: [
        { id: 1, text: "vue-router", done: false },
        { id: 2, text: "vuex", done: false },
        { id: 3, text: "vue-loader", done: false },
        { id: 4, text: "awesome-vue", done: true }
      ],
      newTask: "test"
    };
  }
};
</script>

<style scoped>
.task-list ul li {
  list-style-type: none;
}
</style>
