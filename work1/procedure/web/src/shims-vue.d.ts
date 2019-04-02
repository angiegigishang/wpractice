declare module '*.vue' {
  import Vue from 'vue'
  export default Vue
}

declare module 'vue/types/vue' {
  interface Vue {
    $mg_t: any;
    isPortal?: boolean | undefined;
    showNotify?: any;
    _isValid?: any;
    responseValidate?: any;
    download?: any;
    [propName: string]: any;
  }
  interface VueConstructor {
    [propName: string]: any;
  }
}

