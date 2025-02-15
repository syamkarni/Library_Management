import Vue from "vue";
import VueRouter from "vue-router";

import RegisterView from "../views/auth/RegisterView.vue"
import LoginView from "../views/auth/LoginView"
import CommonHomeView from "../views/home/CommonHomeView.vue"
import AddSection from "../views/addons/AddSection.vue"
import AddBook from "../views/addons/AddBook.vue"

Vue.use(VueRouter)

const routes = [
    {
        path: '/home',
        name: 'Home',
        component: CommonHomeView,  // Set CommonHomeView as the default route
    },
    {
        path:"/register",
        name: "Registration-Page",
        component: RegisterView,
    },
    {
        path:"/login",
        name: "Login-Page",
        component: LoginView,
    },
    {
        path: "/addsection",
        name: "Add-Section",
        component: AddSection,
    },{
        path: '/addbook/:sectionId',
        name: "AddBook",
        component: AddBook,
    }
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router