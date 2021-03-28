import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    folder_data: {},
  },
  getters: {
    GET_FOLDERS(state) {
      return state.folder_data.folders;
    },
    GET_FILES(state) {
      return state.folder_data.files;
    },
    GET_THIS_FOLDER_DATA(state){
      return state.folder_data.this_folder_data;
    }
  },
  mutations: {
    SET_FOLDER_DATA: (state, folder_data) => {
      state.folder_data = folder_data;
    }
  },
  actions: {
    LOAD_FOLDER_DATA({commit}, id=null){
      let url = ''
      if(id == null) {
        url = 'http://localhost:8000/api/folders/'
      } else {
        url = 'Http://localhost:8000/api/folders/?id=' + id
      }
      return axios(url, {
        method: 'get'
      }).then((folder_data) => {
        commit("SET_FOLDER_DATA", folder_data.data);
        return folder_data;
      }).catch((err) => {
        console.log(err);
        return err;
      })
    },

    DOWNLOAD(state, url){
      console.log(url)
      return axios.get(
        url, 
        {responseType: 'blob'}
        ).then((response) => {
          console.log(response.data)
          let link = document.createElement('a');
          link.href = url;
          document.body.appendChild(link);
          link.click();
        })
    },

    UPLOAD_FILE(store, formData){
      return axios.post(
        'http://localhost:8000/api/files/upload/', 
        formData
        ).then((response) => {
          console.log("File Uploaded "+response);
          console.log(store.state.folder_data.this_folder_data.id);
          store.dispatch('LOAD_FOLDER_DATA', store.state.folder_data.this_folder_data.id);
        }).catch((err) => {
          console.log(err)
        })
    },

    CREATE_NEW_FOLDER(store,folderName){
      let url = 'http://localhost:8000/api/folders/create/'
      return axios.post(url, {
          parent: store.state.folder_data.this_folder_data.id,
          name: folderName
      }).then((res) => {
        console.log(res);
        store.dispatch('LOAD_FOLDER_DATA', store.state.folder_data.this_folder_data.id);
      }).catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
