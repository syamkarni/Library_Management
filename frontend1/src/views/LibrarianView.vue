<template>
  <div>
      <router-link to='/addsection'><button class="fixed-plus-button">Add Section</button></router-link>
      <h1>Librarian Dashboard</h1>
      <div class="container">
        <div class="main-container" v-for="(section, index) in sections" :key="index">
          <div class="d-flex justify-content-between align-items-center">
            <h2>{{ section.name }}</h2>
            <p>{{ formatDate(section.date_created) }}</p>
          </div>
          <p>{{ section.description }}</p>
          <div class="row">
            <div class="col-md-4"
           v-for="book in booksForSection(section.id)"
           :key="book.book_id">
              <div class="custom-container">
                <h5>{{ book.book_name }}</h5>
                <p> hello {{ book.book_author }}</p>
                <p>Pages: {{ book.pages }}</p>
                <p>Content: {{ book.content }}</p>
                <button class="btn btn-dark" @click="editBook(book.id)">Edit</button>
              </div>
            </div>
          </div>
          <div class="d-flex justify-content-center">
            <button class="btn btn-dark" @click="navigateToAddBook(section.id)">+</button>
          </div>
        </div>
      </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'LibrarianView',
  data() {
    return {
      sections: [],
      books: [],
    };
  },
  created() {
    this.fetchSections();
    this.fetchAllBooks();
  },
  methods: {
    navigateToAddBook(sectionId) {
    this.$router.push({ name: 'AddBook', params: { sectionId: sectionId }});
  },
  fetchAllBooks() {
    axios.get('http://127.0.0.1:8081/api/book') // Make sure the URL is correct
      .then(response => {
        this.books = response.data;
      })
      .catch(error => {
        console.error('Error fetching books:', error);
      });
  },
  booksForSection(sectionId) {
    return this.books.filter(book => book.section_id === sectionId);
  },
    fetchSections() {
      // Replace the URL with your actual API endpoint
      axios.get('http://127.0.0.1:8081/api/sections')
        .then(response => {
          this.sections = response.data;
        })
        .catch(error => {
          console.error('Error fetching sections:', error);
        });
    },
    formatDate(dateString) {
      return dateString.split(' ')[0];
    }
  }
};
</script>

<style scoped>
/* CSS styles provided in the question */

.main-container {
  background-color: #333333;
  padding: 20px;
  border-radius: 10px;
  margin-bottom: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
}
.custom-container {
  background-color: #222222;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 15px;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.4);
}
.fixed-plus-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  font-size: 20px;
  padding: 10px 15px;
  border-radius: 15%;
  background-color: #c2c6cb;
  color: rgb(0, 0, 0);
  border: none;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  cursor: pointer;
}
</style>
