const data = 'text_data'

const dictData = {
    data: 'text_dictData',
    consoleLogInfo: function() {
        console.log(this.data) //text_dictData
        console.log(data) //text_data
    }
}

dictData.consoleLogInfo();