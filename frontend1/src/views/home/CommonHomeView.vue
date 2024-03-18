<template>
    <div class="main-body">
      <head>
        <title>Bootstrap Navbar</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      </head>
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container-fluid">
          <a class="navbar-brand" href="#">Navbar</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" 
                  data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" 
                  aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
              <div class="navbar-nav">
                  <a class="nav-link active" aria-current="page" href="#">Home</a>
                  <a class="nav-link" href="#">Features</a>
                  <a class="nav-link" href="#">Pricing</a>
                  <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
              </div>

              <form class="d-flex ms-auto">
                  <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                  <button class="btn btn-outline-success" type="submit">Search</button>
              </form>

              <button class="btn btn-outline-danger ms-2" type="button" @click="logout">Sign Out</button>
          </div>
      </div>
  </nav>
      <div class="Navbar_padding">
        <UserHome v-if="userRole == 'user'" />
        <AdminHome v-if="userRole == 'admin'" />
        <LibrarianHome v-if="userRole == 'librarian'" />
      </div>
      <div class="bottom-bar">
        <p>Footer content here</p>
    </div>
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
  .main-body {
  background-color: #121212; /* Dark background */
  color: #ffffff; /* Light text */
  padding-top: 20px;
        }
  .Navbar_padding {
    padding-top: 56px; /* Adjust according to your navbar's height */
  }
  .bottom-bar {
            
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #343a40; /* Assuming this is your navbar color */
            color: white;
            text-align: center;
            padding: 0.25px 0;
        }
  </style>
  