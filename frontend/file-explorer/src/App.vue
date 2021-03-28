<template>
  <v-app id="inspire">
    <v-app-bar
      app
      dense
      dark
    >
      <v-toolbar-title>File Explorer</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-dialog
        v-model="dialogCreateFolder"
        max-width="290"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
            color="success"
            class="ma-2"
            dark
            v-bind="attrs"
            v-on="on"
            >
              <v-icon left>
                mdi-folder
              </v-icon>
              New Folder
            </v-btn>
          </template>
          <v-card>
            <v-card-title class="headline">
              Create New Folder
            </v-card-title>
            <v-card-text>
              <v-text-field
              v-model="fileNameField"
              label="Folder name"
              :rules="rulesFileName"
              hide-details="auto"
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
                <v-btn
                color="green darken-1"
                text
                @click="createNewFolder"
                >
                  Create
                </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog
        v-model="dialogUploadFile"
        max-width="290"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
            color="success"
            class="ma-2"
            dark
            v-bind="attrs"
            v-on="on"
            >
              <v-icon left>
                mdi-upload
              </v-icon>
              Upload File
            </v-btn>
          </template>
          <v-card>
            <v-card-title class="headline">
              Upload File
            </v-card-title>
            <v-card-text>
              <v-text-field
              v-model="uploadFileNameField"
              label="File name"
              :rules="rulesFileName"
              hide-details="auto"
              ></v-text-field>
              <v-file-input
              :rules="rulesFileName"
              accept="*"
              label="File input"
              v-model="uploadFile"
              ></v-file-input>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
              color="green darken-1"
              text
              @click="uploadingFile"
              >
                Upload
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-btn
        tile
        color="success"
        class="ml-2"
        @click="DOWNLOAD('http://localhost:8000/api/folders/download/'+ GET_THIS_FOLDER_DATA.id)"
        >
          <v-icon left>
            mdi-download
          </v-icon>
          Download Folder
        </v-btn>
    </v-app-bar>

    <v-main>
      <v-container
        v-if="GET_THIS_FOLDER_DATA"
      >
        <v-row
        justify="space-around"
        >
          <v-col>
            <h1>{{ GET_THIS_FOLDER_DATA.name }}</h1>
          </v-col>
        </v-row>
        <v-row
          v-if="GET_THIS_FOLDER_DATA.parent != null"
        >
          <v-col>
            <v-btn
              color="success"
              fab
              x-large
              dark
              @click="backToParent(GET_THIS_FOLDER_DATA.parent)"
            >
              <v-icon>mdi-arrow-left-circle</v-icon>
            </v-btn>
          </v-col>
        </v-row>
        <v-row
        v-if="GET_FOLDERS.length > 0"
        >
          <v-col cols="12"><h2>Folders</h2></v-col>
          <v-col
            v-for="folder in GET_FOLDERS"
            :key="folder.id"
            cols="2"
          >
            <v-card
            flat
            hover
            @click="changeFolder(folder.id)"
            >
              <v-img
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTj3VcKBVIm_kWLd5zLwu9k0Xl3kZy_-UkwplzFIYKiehVHJFL80cL2iyPm8FZtZF8dw5Y&usqp=CAU"
                height="150px"
              ></v-img>
              <v-card-title>
                {{folder.name}}
              </v-card-title>
            </v-card>
          </v-col>
        </v-row>
        <v-row
        v-if="GET_FILES.length > 0"
        >
          <v-col cols="12"><h2>Files</h2></v-col>
          <v-col
            v-for="file in GET_FILES"
            :key="file.id"
            cols="2"
          >
            <v-card
            flat
            hover
            @click="DOWNLOAD('http://localhost:8000/api/files/download/'+file.id)"
            >
              <v-img
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxVNXkoCd8d5kBoNLcyJ3Bh--phDgW5VO5H2irUute-yZxNDcMGN36i2fR5KlMLjlRKMw&usqp=CAU"
                height="180px"
              ></v-img>
              <v-card-title>
                {{file.name}}
              </v-card-title>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'
  export default {
    data: () => ({
      dialogCreateFolder: false,
      dialogUploadFile: false,
      fileNameField: '',
      uploadFileNameField: '',
      uploadFile: null,
      rulesFileName: [
        value => !!value || 'Required.',
      ],
    }),
    computed: {
      ...mapGetters([
        'GET_FOLDERS',
        'GET_FILES',
        'GET_THIS_FOLDER_DATA'
      ])
    },
    methods: {
      ...mapActions([
        'LOAD_FOLDER_DATA',
        'CREATE_NEW_FOLDER',
        'DOWNLOAD',
        'UPLOAD_FILE',
      ]),
      changeFolder(id){
        this.LOAD_FOLDER_DATA(id);
      },
      backToParent(parent){
        this.LOAD_FOLDER_DATA(parent);
      },
      createNewFolder() {
        this.CREATE_NEW_FOLDER(this.fileNameField);
        this.dialogCreateFolder = false;
      },

      uploadingFile(){
        if (this.uploadFile){
          let fd= new FormData();
          fd.append("file", this.uploadFile, this.uploadFileNameField);
          fd.append("name", this.uploadFileNameField);
          fd.append("folder", this.GET_THIS_FOLDER_DATA.id);
          this.UPLOAD_FILE(fd);
        } else {
          console.log("Not file");
        }
        this.dialogUploadFile = false;
      },
    },
    mounted(){
      this.LOAD_FOLDER_DATA(1)
    },
  }
</script>