import Vue from 'vue'
declare global {
    namespace Personal {
        class Verify extends Vue {
            $t?: any;
            $mg_t?: any;
            showNotify?: any;
            _isValid?: any;
            responseValidate?: any;
            download?: any;
            isPortal?: boolean;
        }
    }
    interface chooseData {
        worksheet_id: string;
        name: string | number;
        start_time: string;
        end_time: string;
        procedure: Array<{
            name: string,
            code: string,
            description: string
        }>;
        num: string;
        state: string;
        person_id: string;
        person_name: string;
        completed_count?: number;
    }

    interface allPro {
        code: string;
        description: string;
        name: string;
    }

    interface historyHeaderData {
        device_info: {
            name: string,
            code: string,
            description: string
        };
        worksheet_info: {
            worksheet_id: string,
            start_time: string,
            num: string,
            end_time: string,
            product: string
        },
        state: string
    }

    interface historyRunningData {
        procedure_info: {
            code: string,
            name: string,
            description: string
        }[];
        data: {
            mark: string,
            start: string,
            person_name: string,
            person_id: string,
            product_info: string,
            end: string
        }[]
    }
    type historyDetailData = {
        mark: string,
        start: string,
        person_name: string,
        person_id: string,
        product_info: {
            code: string,
            description: string,
            name: string,
            component_num: string
        },
        end: string,
        procedure_name: string
    }[]

    type startOpData = {
        worksheet_id: string,
        device_code: string,
        person_id: string,
        person_name: string
    }

    type startOp = {
        worksheet_id: string,
        device_code: string,
        bind_time: string,
        state: string,
        person_id: string,
        person_name: string
    }

    type stopOpData = {
        worksheet_id: string,
        device_code: string
    }

    type stopOp = {
        worksheet_id: string,
        device_code: string,
        state: string,
        unbind_time: string,
        bind_time: string,
        person_id: string,
        person_name: string
    }

    type postMarkData = {
        worksheet_id: string,
        device_code: string,
        procedure_code: string,
        mark: string,
        mark_time: string,
        state: string
    }

    type postMark = {
        code: string,
        description: string,
        name: string,
        component_num: string,
        person_id: string,
        person_name: string
    }

    interface Store {
        httpBody?: any;
        pageTitle?: string;
        titles: allPro[];
        [propName: string]: any;
    }
    var process: NodeJS.Process
}
