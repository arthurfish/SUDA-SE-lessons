<template>
  <div class="app-container">
    <div class="user">
      <strong>{{ user.name }}</strong><br />
      <small>{{ user.dept }} &nbsp;&nbsp; {{ user.roles }}</small>
    </div>
    <el-row class="user-content" style="">
      <el-col :span="6" class="profile">
        <img class="user-avatar" src="@/assets/img/avatar.gif" /><br />
        <p>
          <span class="title"><em class="el-icon-phone"></em>&nbsp;&nbsp;{{ user.phone }}</span>
        </p>
        <p>
          <span class="title"><em class="el-icon-message"></em>&nbsp;&nbsp;{{ user.email }}</span>
        </p>
        <p>
          <span class="title"><em class="el-icon-open"></em>&nbsp;&nbsp;{{
              user.status == '1' ? '启用' : '禁用'
          }}</span>
        </p>

      </el-col>
      <el-col :span="18" style="padding-left:10px;">
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="个人资料" name="profile">
            <el-form label-width="80px">
              <h4>基本信息</h4>
              <el-form-item label="编号">
                <span> {{ user.account }}</span>
              </el-form-item>
              <el-form-item label="姓名">
                <span>{{ user.name }}</span>
              </el-form-item>
              <el-form-item label="性别">
                <span> {{ (user.sex = 1 ? '男' : '女') }}</span>
              </el-form-item>

              <h4>联系信息</h4>
              <el-form-item label="手机">
                <span>{{ user.phone }}</span>
              </el-form-item>
              <el-form-item label="邮箱">
                <span> {{ user.email }}</span>
              </el-form-item>

            </el-form>
          </el-tab-pane>
          <el-tab-pane label="最近活动" name="timeline">
            <el-timeline :reverse="reverse" style="margin-top:15px;padding-left:2px;">
              <el-timeline-item v-for="(activity, index) in activities" :key="index" :timestamp="activity.createTime">
                {{ activity.logname }}
              </el-timeline-item>
            </el-timeline>
          </el-tab-pane>
          <el-tab-pane label="修改密码" name="updatePwd">
            <el-form ref="form" :model="form" label-position="left" label-width="80px">
              <el-row>
                <el-col :span="24">
                  <el-form-item label="原密码">
                    <el-input type="password" v-model="form.oldPassword"></el-input>
                  </el-form-item>
                </el-col>
                <el-col :span="24">
                  <el-form-item label="新密码" prop="password">
                    <el-input type="password" v-model="form.password" minlength="5"></el-input>
                  </el-form-item>
                </el-col>

                <el-col :span="24">
                  <el-form-item label="重复密码">
                    <el-input type="password" v-model="form.rePassword"></el-input>
                  </el-form-item>
                </el-col>
              </el-row>
              <el-form-item>
                <el-button type="primary" @click="updatePwd">{{
                    $t('button.submit')
                }}</el-button>
              </el-form-item>
            </el-form>
          </el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
  </div>
</template>

<script src="./profile.js"></script>

<style rel="stylesheet/scss" lang="scss" scoped>
@import 'src/styles/common.scss';

.el-form-item {
  margin-bottom: 15px;
}
</style>
