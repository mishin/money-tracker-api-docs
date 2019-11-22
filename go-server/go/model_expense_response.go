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

type ExpenseResponse struct {

	// 支出ID
	Id string `json:"id,omitempty"`

	// 支出額
	Amount int32 `json:"amount,omitempty"`

	// 支出日付
	Date string `json:"date,omitempty"`

	// 支出内容
	Content string `json:"content,omitempty"`
}
