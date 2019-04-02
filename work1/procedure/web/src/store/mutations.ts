export const updateHttpBody = (state: Store, data: any) => {
  if (data) {
    state.httpBody = data
  }
}
// 设置页面title显示
export const setPageTitle = (state: Store, title: string) => {
  state.pageTitle = title
}

export const putTitles = (state: Store, titles: allPro[]) => {
  if (titles) {
    state.titles = titles
  }
}
