window.onload = function () {
    const Info = () => import('/vue/info.vue')
    const Status = () => import('/vue/info.vue')
    const routes = [
        {path: '/info', component: Info},
        {path: '/status', component: Status}
    ]
    new Vue({
        el: '#app',
        router: new VueRouter({routes}),
        vuetify: new Vuetify(),
        data: () => ({
            drawer: null,
            item: null,
            items: [
                {text: '设备信息', icon: 'mdi-clock', url: '/info'},
                {text: '设备状态', icon: 'mdi-account', url: '/status'},
                {text: 'GPIO', icon: 'mdi-flag'},
            ]
        }),
        created() {
            document.querySelector("#app").removeAttribute("hidden");
        }
    })
}