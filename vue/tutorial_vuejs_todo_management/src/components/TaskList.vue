<template>
    <div>
        {{ msg }}
        <form>
            <button>Add Task</button>
            <button>Delete Finished Tasks</button>
            <p>input: <input type="text"></p>
            <p>task:</p>
        </form>
        <div class="task-list">
            <ul>
                <li><label class="task-list__item"><input type="checkbox"><button>Edit</button>vue-router</label></li>
                <li><label class="task-list__item"><input type="checkbox"><button>Edit</button>vuex</label></li>
                <li><label class="task-list__item"><input type="checkbox"><button>Edit</button>vue-loader</label></li>
                <li><label class="task-list__item--checked"><input type="checkbox"><button>Edit</button>awesome-vue</label></li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
  name: "tasklist",
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
  }
};
</script>

<style scoped>
.task-list ul li {
  list-style-type: none;
}
</style>
