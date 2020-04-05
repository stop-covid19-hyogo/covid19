import dayjs from 'dayjs'

/**
 * Get datetime string formatted ISO8601(YYYY-MM-DDTHH:mm:ss)
 *
 * @param dateString - Parsable string by dayjs
 */
export const convertDatetimeToISO8601Format = (dateString: string): string => {
  return dayjs(dateString).format('YYYY-MM-DDTHH:mm:ss')
}

/**
 * Get datetime string formatted Datetime(YYYY/MM/DD HH:mm)
 *
 * @param dateString - Parsable string by dayjs
 */
export const convertISO8601FormatToDatetime = (dateString: string): string => {
  return dayjs(dateString).format('YYYY/MM/DD HH:mm')
}

/**
 * Get date string formatted ISO8601(YYYY-MM-DD)
 *
 * @param dateString- Parsable string by dayjs
 */
export const convertDateToISO8601Format = (dateString: string): string => {
  return dayjs(dateString).format('YYYY-MM-DD')
}
