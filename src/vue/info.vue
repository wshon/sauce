export default {
    template: `<v-row>
  <v-col cols="12" sm="6" offset-sm="3">
    <v-card>
      <v-list two-line disabled>
        <template v-for="(item, index) in items">
          <v-subheader v-if="item.header" :key="item.header" v-text="item.header"></v-subheader>
          <v-divider v-else-if="item.divider" :key="index" :inset="item.inset"></v-divider>
          <v-list-item v-else :key="item.title" @click="">
            <v-list-item-avatar v-if="item.avatar">
              <img :src="item.avatar">
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title v-html="item.title"></v-list-item-title>
              <v-list-item-subtitle v-html="info[item.key]"></v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-card>
  </v-col>
</v-row>`,
    data: () => ({
        info: {},
        items: [
            {header: '设备信息'},
            {divider: true, inset: false},
            {key: 'machine', title: '设备平台',},
            {divider: true, inset: false},
            {key: 'node', title: '设备名称',},
            {divider: true, inset: false},
            {key: 'processor', title: '处理器',},
            {divider: true, inset: false},
            {key: 'system', title: '系统平台',},
            {divider: true, inset: false},
            {key: 'release', title: '发布版本',},
            {divider: true, inset: false},
            {key: 'version', title: '发布信息',},
        ],
    }),
    created() {
        axios.get('/info/base').then(res => res.data).then((res) => {
            console.log(res);
            this.info = res
        }).catch((error) => {
            console.log(error);
        });
    },
}