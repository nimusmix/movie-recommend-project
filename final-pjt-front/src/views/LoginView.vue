<template>
  <div class="all">
    <div class="logo t-d-none">20.</div>
    <h3 class="h3">로그인</h3>
    <form @submit.prevent="login" class="login-form">
      <label for="username">유저 이름을 입력해주세요.</label>
      <input type="text" id="username" class="user-input" v-model="username"><br>

      <label for="password">비밀번호를 입력해주세요.</label>
      <input type="password" id="password" class="user-input" v-model="password">

      <p v-if="errMsg" class="err-msg">{{ errMsg }}</p><br>
      <input type="submit" class="main-button selected mb-1" value="로그인">
      <router-link style="margin-top:4px" class="sign-up" :to="{ name: 'SignupView' }">회원가입</router-link>
    </form>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
      errMsg: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password
      this.errMsg = null

      axios({
        method: 'post',
        url: `${this.API_URL}/accounts/login/`,
        data: {
          username,
          password,
        }
      })
        .then((res) => {
          const user = {
            username: this.username,
            token: res.data.key
          }
          this.$store.commit('SAVE_USER', user)
        })
        .then(() => {
          this.$store.dispatch('getLoginUser')
          this.$router.push({ name: 'HomeView' })
        })
        .catch(() => {
          this.errMsg = '입력한 정보를 확인해주세요.'
        })
    },
  },
  computed:{
    API_URL(){
      return this.$store.state.API_URL
    }
  }
}
</script>

<style lang="scss">
  .all {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .logo {
      font-size: 100px;
    }

    .login-form {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin-top: 20px;
    }
  }
  .sign-up{
    color: var(--disable-color);
  }
</style>