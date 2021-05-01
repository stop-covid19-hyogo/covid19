type DataType = {
  children: [
    {
      attr: '陽性患者数'
      value: number
      children: [
        {
          attr: '入院中'
          value: number
          children: [
            {
              attr: '軽症・中等症'
              value: number
            },
            {
              attr: '重症'
              value: number
            }
          ]
        },
        {
          attr: '宿泊療養'
          value: number
        },
        {
          attr: '入院・宿泊療養調整等'
          value: number
          children: [
            {
              attr: '入院調整'
              value: number
            }
          ]
        },
        {
          attr: '自宅療養'
          value: number
        },
        {
          attr: 'その他医療機関福祉施設等'
          value: number
        },
        {
          attr: '死亡'
          value: number
        },
        {
          attr: '退院'
          value: number
        }
      ]
    }
  ]
}

type ConfirmedCasesType = {
  陽性者数: number
  入院中: number
  軽症中等症: number
  重症: number
  宿泊療養: number
  入院宿泊療養調整等: number
  入院調整: number
  自宅療養: number
  その他: number
  死亡: number
  退院: number
}

interface ChildData {
  attr: string
  value: number
}

type ChildDataType = {
  attr?: string
  value?: number
  children?: ChildData[]
}

function getSelectedItem(data: DataType, key: string) {
  let result: number | undefined
  const recursiveSearch = (data: ChildDataType) => {
    if (result) {
      return
    }
    if (data.attr === key) {
      result = data.value
    } else if (data.children) {
      data.children.forEach((child: ChildDataType) => {
        if (result) {
          return
        }
        recursiveSearch(child)
      })
    }
  }
  recursiveSearch(data)

  return result || 0
}

/**
 * Format for *Chart component
 *
 * @param data - Raw data
 */
export default (data: DataType) => {
  return {
    陽性者数: getSelectedItem(data, '陽性患者数'),
    入院中: getSelectedItem(data, '入院中'),
    軽症中等症: getSelectedItem(data, '軽症・中等症'),
    重症: getSelectedItem(data, '重症'),
    宿泊療養: getSelectedItem(data, '宿泊療養'),
    入院宿泊療養調整等: getSelectedItem(data, '入院・宿泊療養調整等'),
    入院調整: getSelectedItem(data, '入院調整'),
    自宅療養: getSelectedItem(data, '自宅療養'),
    その他: getSelectedItem(data, 'その他医療機関福祉施設等'),
    死亡: getSelectedItem(data, '死亡'),
    退院: getSelectedItem(data, '退院'),
  } as ConfirmedCasesType
}
