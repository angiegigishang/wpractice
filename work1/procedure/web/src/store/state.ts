// 防止刷新丢失state数据 先检查sessionStorate

let state: Store = {
  httpBody: null,
  pageTitle: '',
  titles: []
}

// if (sessionStorage.getItem('state')) {
//   state = JSON.parse(sessionStorage.getItem('state'))
//   sessionStorage.removeItem('state')
// }

export default state
