<template>
  <div class="app-container">
    <el-col :span="12">
      <el-row>
        <div class="tip">
          请上传要提取的图片
        </div>
        <el-upload class="upload-demo" action="" :limit="10" :http-request="uploadImg" accept=".jpg,.jpeg,.png,.bmp"
          style="padding-bottom:24px;">
          <el-button type="primary">点击上传</el-button>
        </el-upload>
      </el-row>
      <el-row>
        <div class="tip">
          请输入需要提取的信息（中文逗号隔开，尽可能描述准确）
        </div>
        <el-input v-model="input" type="input" :rows="8" style="padding-bottom:10px;" />
      </el-row>
      <el-row style="padding-top:10px;padding-bottom:30px;">
        <div class="tip">
          模型选择
        </div>
        <el-select v-model="value" class="m-2" placeholder="Select" size="large" style="padding-right:24px">
          <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
        </el-select>
        <el-button type="primary" :loading='loading'  @click="imageCorrect()">开始提取</el-button>
        <el-button type="basic"  @click="handleDownload('demo')">导出Excel</el-button>
      </el-row>
      <div v-show="visible" class="tip">
        图片识别和识别结果：
      </div>
      <el-table v-loading="loading" id="excel_table" :data="tableData" style="width: 100%">
        <el-table-column prop="prompt" label="Prompt"></el-table-column>
        <el-table-column prop="value" label="Value"></el-table-column>
        <el-table-column prop="prob" label="Prob"></el-table-column>
        <el-table-column prop="start" label="Start"></el-table-column>
        <el-table-column prop="end" label="End"></el-table-column>
      </el-table>
    </el-col>
    <el-col :span="10">
      <div class="demo-image__error" style="text-align: center;">
        <div class="block" style="padding-top:24px;padding-bottom:10px;">
          <span class="demonstration"></span>
        </div>
        <el-image style="padding-left:48px;" :src="imageUrl" :fit="fit">
          <template #error>
            <div class="image-slot">
              <el-icon><icon-picture /></el-icon>
            </div>
          </template>
        </el-image>
      </div>
    </el-col>
  </div>
</template>

<script >
import axios from 'axios'
import { saveAs } from 'file-saver'
import { ref } from 'vue'
import FileSaver from 'file-saver'
// full import
import * as XLSX from 'xlsx';
// named imports
import { write, utils } from 'xlsx';



export default {
  data() {
    return {
      fileData: '',
      input: '',
      visible: false,
      tableData: [],
      imageUrl: '',
      fit: 'cover',
      loading: false,
      value: ref(1),
      options: [
        {
          value: 1,
          label: 'ERNIE-3.0',
        },
        {
          value: 2,
          label: 'gpt-3.5-turbo',
        }
      ]
    }
  },

  beforeCreate() {
    // 读取文件
    FileReader.prototype.reading = function ({ encode } = 'pms') {
      const bytes = new Uint8Array(this.result) // 无符号整型数组
      const text = new TextDecoder(encode || 'UTF-8').decode(bytes)
      return text
    }
    /* 重写readAsBinaryString函数 */
    FileReader.prototype.readAsBinaryString = function (f) {
      // 如果this未重写onload函数，则创建一个公共处理方式
      if (!this.onload) {
        this.onload = e => { // 在this.onload函数中，完成公共处理
          const rs = this.reading()
          console.log(rs)
        }
      }
      this.readAsArrayBuffer(f) // 内部会回调this.onload方法
    }
  },
  methods: {

    handleDownload(name) {
      let table = document.getElementById("excel_table")
      let et = utils.table_to_book(table)
      let output = write(et, {
        bookType: "xlsx",
        bookSST: true,
        type: "array"
      })

      try {
        FileSaver.saveAs(new Blob([output], { type: "application/octet-stream" }), `${name}.xlsx`)
      } catch (e) { }

      return output
    },


    // 储存选择的file文件
    uploadImg(file) {
      this.fileData = file.file
      console.log(file.file)
      this.$message({
        showClose: true,
        message: '图片上传成功！',
        type: 'success'
      })
      this.imageUrl = URL.createObjectURL(file.file)
    },
    // 保存识别结果
    saveResult() {
      // console.log(this.fileList)
      var tempData = this.imgCscResult
      if (tempData === '') {
        this.$message({
          showClose: true,
          message: '识别结果内容为空！',
          type: 'warning'
        })
      } else {
        var tempResult = new Blob([tempData], { type: 'text/plain;charset=utf-8' })
        saveAs(tempResult, '图片识别结果.txt')
      }
    },
    imageCorrect() {
      var that = this
      that.loading = true
      if (that.fileData === '') {
        this.$message({
          showClose: true,
          message: '请先选择要进行识别的图片文件！',
          type: 'warning'
        })
        that.imgCscResult = ''
        that.visible = false
        return
      }
      var config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        params: {
          key: that.input,
          value: that.value
        }
      }
      var form = new FormData()
      form.append('file', that.fileData)
      // 请求后端API服务，请求方法为post
      axios.post('http://127.0.0.1:8000/v1/imageCorrect', form, config).then((response) => {
        console.log(response)
        that.imgCscResult = response.data.correctionResults
        that.tableData = response.data.correctionResults
        console.log(that.tableData)
        that.visible = true
        that.loading = false
        that.$message({
          showClose: true,
          message: '图片识别完成！',
          type: 'success'
        })
      }).catch((error) => {
        console.log(error)
        that.imgCscResult = ''
        that.visible = false
        that.$message({
          showClose: true,
          message: '请求出现异常！',
          type: 'error'
        })
      })
    }
  }
}

</script>

<style scoped>
.tip {
  font-family: Helvetica Neue, Arial, Helvetica, sans-serif;
  font-size: 14px;
  font-weight: normal;
  margin-bottom: 20px;
  margin-bottom: 10px;
}
</style>
