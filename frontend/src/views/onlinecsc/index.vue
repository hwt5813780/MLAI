<template>
  <div class="app-container">
    <el-col :span="12">
    <div class="tip">
      请输入需要提取的文本:
    </div>
    <el-input v-model="textarea" type="textarea" :disabled="stage" :rows="11" placeholder="请输入" clearable />
    <div class="tip" style="padding-top:10px">
      请输入提取的信息类型（用逗号隔开）:
    </div>
    <el-input v-model="input" type="input" :disabled="stage" :rows="11" placeholder="请输入" clearable/>
    <div style="padding-top:10px;padding-bottom:10px;">
      <el-button type="primary" @click="errorCorrect()" :loading='loading'>开始提取</el-button>
      <el-button type="basic"  style="margin-left:24px;margin-top:16px;" @click="handleDownload('text-demo')">导出Excel</el-button>
    </div>

    <div v-show="visible" class="tip">
      ChatGPT:
    </div>
    <el-input v-show="visible" v-model="result" type="textarea" :rows="11" />
    </el-col>
    <el-col :span="12">
    <el-table v-loading="loading" id="excel_table" :data="tableData" style="width: 100%;margin-left:48px;margin-right:48px;">
        <el-table-column prop="prompt" label="Prompt"></el-table-column>
        <el-table-column prop="value" label="Value"></el-table-column>
    </el-table>
    </el-col>
  </div>
</template>

<script>
import axios from 'axios'
import { saveAs } from 'file-saver'
import FileSaver from 'file-saver'
import { write, utils } from 'xlsx';

export default {
  data() {
    return {
      textarea: '',
      input: '',
      result: '',
      stage: false,
      visible: false,
      fileList: '',
      tableData: [],
      loading: false,
    }
  },
  beforeCreate() {
    // 读取文件
    FileReader.prototype.reading = function({ encode } = 'pms') {
      const bytes = new Uint8Array(this.result) // 无符号整型数组
      const text = new TextDecoder(encode || 'UTF-8').decode(bytes)
      return text
    }
    /* 重写readAsBinaryString函数 */
    FileReader.prototype.readAsBinaryString = function(f) {
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

    //导出excel
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
    errorCorrect() {
      var that = this
      that.loading = true
      var context = that.textarea
      var key = that.input
      if (context === '' || key === '') {
        this.$message({
          showClose: true,
          message: '输入内容不能为空',
          type: 'warning'
        })
        that.result = ''
        that.visible = false
      } else {
        // 请求后端API服务，请求方法为post，请求体字段为json格式 text
        axios.post('http://127.0.0.1:8000/v1/textCorrect', {
          text: that.textarea,
          key: that.input
        }).then((response) => {
          that.result = response.data.correctionResults.toString()
          that.tableData = response.data.correctionResults
          that.visible = true
          that.loading = false
          that.$message({
            showClose: true,
            message: 'Success！',
            type: 'success'
          })
        }).catch((error) => {
          console.log(error)
          that.result = ''
          that.visible = false
          that.$message({
            showClose: true,
            message: '请求出现异常！',
            type: 'error'
          })
        })
      }
    },
    beforeUpload(file) {
      this.fileList = [file]
      // 读取txt文件
      this.read(file)
      this.$message({
        showClose: true,
        message: 'txt文本内容导入成功！',
        type: 'success'
      })
      return false
    },
    read(f) {
      const rd = new FileReader()
      var that = this
      rd.onload = e => {
      // this.readAsArrayBuffer函数内，会回调this.onload函数。在这里处理结果
        const cont = rd.reading({ encode: 'UTF-8' })
        console.log(cont)
        that.textarea = cont
      }
      rd.readAsBinaryString(f)
    },
    saveResult() {
      var tempData = this.result
      if (tempData === '') {
        this.$message({
          showClose: true,
          message: '输入内容为空！',
          type: 'warning'
        })
      } else {
        var tempResult = new Blob([tempData], { type: 'text/plain;charset=utf-8' })
        saveAs(tempResult, 'ChatGPT结果.txt')
      }
    }
  }
}
</script>

<style scoped>
  .tip {
    font-family: Helvetica Neue, Arial, Helvetica, sans-serif;
	font-size: 14px;
	font-weight:normal;
	margin-top: 10px;
  margin-bottom: 10px;
  }
</style>
