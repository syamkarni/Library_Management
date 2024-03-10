<template>
    <div>
      <UserHome v-if="userRole == 'user'" />
      <AdminHome v-if="userRole == 'admin'" />
      <LibrarianHome v-if="userRole == 'librarian'" />
      <!-- Include other common elements here if needed -->
    </div>
  </template>
  
  <script>
  import UserHome from "@/views/UserView.vue";
  import AdminHome from "@/views/AdminView.vue";
  import LibrarianHome from "@/views/LibrarianView.vue";
  
  export default {
    name: "CommonHomeView",
    components: {
      UserHome,
      AdminHome,
      LibrarianHome
    },
    data() {
      return {
        userRole: localStorage.getItem('userRole') // Assuming the user's role is stored in localStorage
      };
    },
    // include other methods, computed properties, etc., as needed
  };
  </script>
  
  <style scoped>
  /* Your styles here */
  </style>
  