/*
 * Money Tracker API
 *
 * This is a money tracker api
 *
 * API version: 1.0.0
 * Contact: kawakawaryuryu@hotmail.co.jp
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi

type ExpenseRequest struct {

	// 支出額
	Amount int32 `json:"amount"`

	// 支出日付
	Date string `json:"date"`

	// 支出内容
	Content string `json:"content"`
}
