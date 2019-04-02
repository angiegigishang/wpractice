// 表格数据转换
function parseTableHandle (data) {
  return data.map((row, nRowIndex) => {
    let oRow = {}
    row.forEach((v, index) => {
      oRow[`col${index}`] = v
    })
    // 记录行的索引＝》方便找到元素
    oRow['colindex'] = nRowIndex
    oRow['rowspan'] = 0
    oRow['l_rowspan'] = 0
    return oRow
  })
}

// 判断数据是否为对象
function isObject (value) {
  let result = Object.prototype.toString.call(value)
  return result === '[object Object]'
}

export {
  parseTableHandle,
  isObject
}
