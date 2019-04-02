// 防止刷新丢失state数据 先检查sessionStorate

let state = {
  httpBody: null,
  pageTitle: ''
}

// if (sessionStorage.getItem('state')) {
//   state = JSON.parse(sessionStorage.getItem('state'))
//   sessionStorage.removeItem('state')
// }

export default state
