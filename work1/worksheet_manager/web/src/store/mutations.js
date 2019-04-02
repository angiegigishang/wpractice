export const updateHttpBody = (state, data) => {
  if (data) {
    state.httpBody = data
  }
}
// 设置页面title显示
export const setPageTitle = (state, title) => {
  state.pageTitle = title
}
