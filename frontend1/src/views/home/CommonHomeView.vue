<template>
    <div>
      <head>
        <title>Bootstrap Navbar</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      </head>
      
              <button @click="logout">Logout</button>

      <UserHome v-if="userRole == 'user'" />
      <AdminHome v-if="userRole == 'admin'" />
      <LibrarianHome v-if="userRole == 'librarian'" />
      
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
    methods: {
    logout() {
      // Clear user data from localStorage
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      localStorage.removeItem('user_mail');
      localStorage.removeItem('userRole');

      // Redirect to login page
      this.$router.push('/login');
    }
  }
    // include other methods, computed properties, etc., as needed
  };
  </script>
  
  <style scoped>
  /* Your styles here */
  </style>
  