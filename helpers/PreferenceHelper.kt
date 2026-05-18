package com.outrageousstorm.helpers

import android.content.Context
import android.content.SharedPreferences

class PreferenceHelper(context: Context) {
    private val prefs: SharedPreferences = context.getSharedPreferences("outrageousstorm", Context.MODE_PRIVATE)

    fun setString(key: String, value: String) = prefs.edit().putString(key, value).apply()
    fun getString(key: String, default: String = ""): String = prefs.getString(key, default) ?: default

    fun setInt(key: String, value: Int) = prefs.edit().putInt(key, value).apply()
    fun getInt(key: String, default: Int = 0): Int = prefs.getInt(key, default)

    fun setBoolean(key: String, value: Boolean) = prefs.edit().putBoolean(key, value).apply()
    fun getBoolean(key: String, default: Boolean = false): Boolean = prefs.getBoolean(key, default)

    fun remove(key: String) = prefs.edit().remove(key).apply()
    fun clear() = prefs.edit().clear().apply()
}
