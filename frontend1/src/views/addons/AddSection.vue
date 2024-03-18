<template>
  <div class="add-section-container">
    <h1>Add New Section</h1>
    <form @submit.prevent="submitForm">
      <div class="mb-3">
        <label for="sectionName" class="form-label">Section Name</label>
        <input type="text" class="form-control" id="sectionName" v-model="section.name" required>
      </div>
      <div class="mb-3">
        <label for="sectionDescription" class="form-label">Description</label>
        <textarea class="form-control" id="sectionDescription" v-model="section.description"></textarea>
      </div>

      <button type="submit" class="btn btn-primary">Add Section</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'; // Import Axios

export default {
  name: 'AddSection',
  data() {
    return {
      section: {
        name: '',
        description: ''
      }
    };
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8081/api/sections', this.section)
        .then(response => {
          console.log('Response:', response);
          // Handle the response from the server here
          alert("Section added successfully");
          // Clear the form
          this.section = { name: '', description: ''};
        })
        .catch(error => {
          console.error('Error:', error);
          alert("Failed to add section");
        });
    }
  }
};
</script>


<style scoped>
.add-section-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
}
</style>
