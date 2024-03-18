<template>
    <div class="add-book-container">
      <h1>Add New Book</h1>
      <form @submit.prevent="submitForm">
        <!-- Book Name -->
        <div class="mb-3">
          <label for="bookName" class="form-label">Book Name</label>
          <input type="text" class="form-control" id="bookName" v-model="book.book_name" required>
        </div>
  
        <!-- Book Author -->
        <div class="mb-3">
          <label for="bookAuthor" class="form-label">Author</label>
          <input type="text" class="form-control" id="bookAuthor" v-model="book.book_author" required>
        </div>
  
        <!-- Pages in Book -->
        <div class="mb-3">
          <label for="pagesInBook" class="form-label">Pages in Book</label>
          <input type="number" class="form-control" id="pagesInBook" v-model="book.pages_in_book">
        </div>
  
        <!-- Price -->
        <div class="mb-3">
          <label for="price" class="form-label">Price</label>
          <input type="number" class="form-control" id="price" v-model="book.price">
        </div>
  
        <!-- Content -->
        <div class="mb-3">
          <label for="content" class="form-label">Content</label>
          <textarea class="form-control" id="content" v-model="book.content"></textarea>
        </div>
  
  
        <button type="submit" class="btn btn-primary">Add Book</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'AddBook',
    data() {
      return {
        book: {
          book_name: '',
          book_author: '',
          pages_in_book: null,
          price: null,
          content: '',
          section_id: null
        }
      };
    },
    created() {
    this.getSectionIdFromRoute();
  },
    methods: {
      submitForm() {
        axios.post('http://127.0.0.1:8081/api/book', this.book)
          .then(response => {
            console.log('Response:', response);
            alert("Book added successfully");
            this.resetForm();
          })
          .catch(error => {
            console.error('Error:', error);
            alert("Failed to add book");
          });
      },
      resetForm() {
        this.book = {
          book_name: '',
          book_author: '',
          pages_in_book: null,
          price: null,
          content: '',
          section_id: null
        };
      },
      getSectionIdFromRoute() {
      this.book.section_id = this.$route.params.sectionId;
    }
    }
  };
  </script>
  
  <style scoped>
  .add-book-container {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
  }
  </style>
  