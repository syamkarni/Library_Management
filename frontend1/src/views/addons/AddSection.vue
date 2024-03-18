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
      <div class="mb-3">
        <label for="creationDate" class="form-label">Date Created</label>
        <input type="date" class="form-control" id="creationDate" v-model="section.dateCreated" required>
      </div>
      <button type="submit" class="btn btn-primary">Add Section</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'AddSection',
  data() {
    return {
      section: {
        name: '',
        description: '',
        dateCreated: ''
      }
    };
  },
  methods: {
    submitForm() {
      // Here you can handle the form submission.
      // For instance, sending the data to your backend server.
      console.log('Section data:', this.section);
      // Clear the form
      this.section = { name: '', description: '', dateCreated: '' };
      alert("Section added successfully");
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
