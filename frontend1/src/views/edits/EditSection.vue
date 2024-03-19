<template>
    <div class="edit-section-container">
      <h2>Edit Section</h2>
      <form @submit.prevent="updateSection">
        <div class="mb-3">
          <label for="sectionName" class="form-label">Section Name</label>
          <input type="text" class="form-control" id="sectionName" v-model="section.name">
        </div>
        <div class="mb-3">
          <label for="sectionDescription" class="form-label">Description</label>
          <textarea class="form-control" id="sectionDescription" v-model="section.description"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Update Section</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'EditSection',
    props: {
      section: {
        type: Object,
        required: true
      }
    },
    methods: {
      updateSection() {
        axios.put(`http://127.0.0.1:8081/api/sections/${this.section.id}`, this.section)
          .then(response => {
            alert('Section updated successfully');
          })
          .catch(error => {
            console.error('Error updating section:', error);
          });
      }
    }
  }
  </script>
  