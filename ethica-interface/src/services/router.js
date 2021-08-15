import Vue from "vue";
import VueRouter from "vue-router";
import OpusText from "@/components/OpusText";
import Lexicon from "@/components/Lexicon";
import Statistica from "@/components/Statistica";

Vue.use(VueRouter);

const routes = [
    // {
    //     name: "tree",
    //     path: "/tree",
    //     component: TextTree,
    // },
    {
        name: "text",
        path: "/text",
        component: OpusText,
    },
    {
        name: "lexicon",
        path: "/lexicon",
        component: Lexicon
    },
    {
        name: "statistica",
        path: "/statistica",
        component: Statistica
    }
]




export const router = new VueRouter({
    mode: "history",
    routes
})