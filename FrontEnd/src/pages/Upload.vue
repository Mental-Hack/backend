<template>
  <Layout :centered="true">
    <h1 class="title">Пожалуйста, загрузите данные</h1>
  <br />
  <p class="subtitle">Доступна загрузка данных в форматах xlsx или tsv</p>
  <br />
  <el-upload
    class="upload"
    drag
    ref="upload"
    :auto-upload="false"
    :on-change="handleChange"
    :before-remove="handleRemove"
    :limit="1"
  >
    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
    <div class="el-upload__text">Перетащите файл сюда или кликните для загрузки</div>
  </el-upload>
    <el-button class="green-button large-button" type="success" @click="submitUpload" :disabled="disabled">
      Загрузить на сервер
    </el-button>
  </Layout>
</template>


<script setup lang="ts">
import { UploadFilled } from '@element-plus/icons-vue'
import { UploadInstance } from 'element-plus'
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import { ElNotification } from 'element-plus'
import Layout from '@/layouts/Layout.vue'

const upload = ref<UploadInstance>()
const router = useRouter()
const disabled = ref(true)
const extensions = ['xlsx', 'tsv']

const handleChange = (file) => {
  const fileName = file.name.split('.')

  if(extensions.includes(fileName[fileName.length - 1])) {
    disabled.value = false
  } else {
    upload.value.clearFiles()
    showNotification()
  }
}

const handleRemove = () => {
  disabled.value = true
}

const showNotification = () => {
  ElNotification({
    title: 'Пожалуйста, выберите файл с корректным расширением',
  })
}

const submitUpload = () => {
  router.push({name: 'navigation'})
  // upload.value!.submit()

}
</script>

<style lang="sass">
$green: #89e159
$dark: rgb(20, 27, 37)

.el-upload
  background-color: #bfc6dc


.el-upload__text
  color: rgb(20, 27, 37) !important


.green-button
  border: 2px solid $green
  border-radius: 8px
  color: $green
  background-color: #141b25
  padding: 0 10px
  font-size: 16px
  font-weight: 700
  margin: 20px auto
  display: flex
  text-align: center
  cursor: pointer
  align-items: center
  justify-content: center
  height: 40px


.green-button:hover
  color: rgb(20, 27, 37)
  background-color: $green


.el-icon--upload
  color: #5ec724 !important
  opacity: 0.7


.el-button+.el-button
  margin: 20px auto

</style>