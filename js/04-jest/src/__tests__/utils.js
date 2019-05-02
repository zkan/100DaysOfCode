import { getFormattedValue } from '../utils'

test('formats the value', () => {
  expect(getFormattedValue('1234.0')).toBe('1,234.0')
})

// To be able to get window object, enable jest-environment-jsdom
//console.log(window)
