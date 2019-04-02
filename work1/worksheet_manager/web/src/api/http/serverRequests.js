import { _get, _post } from './httpWrap'

export default {
  // declare some methods to communicate with server by using $get | $delete | $post | $put.
  // if you want to access different domain, specify it as the last parameter
  allapps (cbk) {
    _get('api/config/allapps', cbk, null, { baseURL: 'http://192.168.20.186:80' })
  },
  productInfo(cbk) {
     _get( '/worksheet_manage/get_product', cbk )
  },
  worksheetHandler(cbk, succ) {
      _post( '/worksheet_manage/post_worksheet', cbk, succ )
  },
  importExcel(cbk, succ) {
      _post( '/worksheet_manage/excel', cbk, succ )
  }
  // cbk is a customed callback function when the server has response
}
