<template>
  <div class="home">
    <div class="header">
      <h1 class="title">美络 AI Studio</h1>
      <p class="description">Your go-to platform for all things AI</p>
    </div>
    <div class="content">
      <el-card class="card" @click="goToPage1">
        <div class="card-image">
          <img src="https://s1.ax1x.com/2023/03/07/ppZtSiT.png" alt="Image 1">
        </div>
        <div class="card-body" style="text-align: center;">
          <div style="margin-bottom: 24px;font-weight: bold;" >图片信息提取</div>
          <el-button text style="width:100%" class="button" @click="goToPage2">开始使用</el-button>
        </div>
      </el-card>
      <el-card class="card" @click="goToPage2">
        <div class="card-image">
          <img src="https://s1.ax1x.com/2023/03/07/ppZtCz4.png" alt="Image 2">
        </div>
        <div class="card-body" style="text-align: center;">
          <div style="margin-bottom: 24px;font-weight: bold;">文本信息提取</div>
          <el-button text style="width:100%" class="button" @click="goToPage1">开始使用</el-button>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goToPage1() {
      this.$router.push({name: "Onlinecsc"})
    },
    goToPage2() {
      this.$router.push({name: "Imagecsc"})
    },
  },
};
</script>

<style>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 50px 0;
}

.header {
  text-align: center;
  margin-bottom: 30px;
}

.title {
  font-size: 24px;
  font-weight: bold;
}

.description {
  font-size: 14px;
}

.content {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.card {
  width: 300px;
  margin: 20px;
}

.card-image {
  height: 200px;
  overflow: hidden;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-body {
  padding: 20px;
}

.card-body p {
  font-size: 14px;
}
</style>
