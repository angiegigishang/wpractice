import { _get, _post } from './httpWrap'

const request: any = {
  // declare some methods to communicate with server by using $get | $delete | $post | $put.
  // if you want to access different domain, specify it as the last parameter
  allapps (cbk: (res?: any) => void): void {
    _get('api/config/allapps', cbk, null, { baseURL: 'http://192.168.20.186:80' })
  },
  // cbk is a customed callback function when the server has response
  getAllPro (succ: (res: {
    data: allPro[] | null
  }) => void,fail: (err?: any) => void) : void {
    _get('/procedure/get_devices', succ, fail)
  },
  getAllData (code: string, succ: (res?: {
    data: chooseData[] | null
  }) => void, fail: (err?: any) => void): void {
    _get(`/procedure/get_my_worksheets/${code}`, succ, fail)
  },
  getHistoryHeaderData (code: string, succ: (res: {
    data: historyHeaderData[] | null
  }) => void, fail: (err?: any) => void): void {
    _get(`/procedure/get_device_worksheet_info/${code}`, succ, fail)
  },
  getHisRunData (code: string, succ: (res: {
    data: historyRunningData[] | null
  }) => void, fail: (err?: any) => void): void {
    _get(`/procedure/get_device_worksheet/${code}`, succ, fail)
  },
  getHisDetailData (code: string, succ: (res: {
    data: historyDetailData | null
  }) => void, fail: (err?: any) => void): void {
    _get(`/procedure/get_history_data/${code}`, succ, fail)
  },
  startOp (data: startOpData, succ: (res: {
    data: startOp | null
  }) => void, fail: (err?: any) => void): void {
    _post('/procedure/start_worksheet', data, succ, fail)
  },
  stopOp (data: stopOpData, succ: (res: {
    data: stopOp | null
  }) => void, fail: (err?: any) => void) {
    _post('/procedure/end_worksheet', data, succ, fail)
  },
  postMark (data: postMarkData, succ: (res: {
    data: postMark | null
  }) => void, fail: (err?: any) => void): void {
    _post('/procedure/record_mark_time', data, succ, fail)
  }
}
export default request
