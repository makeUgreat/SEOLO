package com.seolo.seolo.presentation

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import com.seolo.seolo.R
import androidx.viewpager2.widget.ViewPager2
import com.seolo.seolo.adapters.CarouselStateAdapter
import com.seolo.seolo.fragments.CardFragment
import com.seolo.seolo.fragments.WorkListFragment

class WorkListActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        installSplashScreen()
        setTheme(android.R.style.Theme_DeviceDefault)
        supportActionBar?.hide()

        // 메인 레이아웃 설정
        setContentView(R.layout.activity_layout)

// ViewPager2와 CarouselStateAdapter 설정
        val viewPager: ViewPager2 = findViewById(R.id.viewPager)
        val adapter = CarouselStateAdapter(this@WorkListActivity)

// CardFragment 인스턴스 생성 및 추가
        adapter.addFragment(WorkListFragment.newInstance("Title 1", "Content 1"))
        adapter.addFragment(WorkListFragment.newInstance("Title 2", "Content 2"))
        adapter.addFragment(WorkListFragment.newInstance("Title 3", "Content 3"))
        adapter.addFragment(WorkListFragment.newInstance("Title 4", "Content 4"))

        viewPager.adapter = adapter
    }
}

