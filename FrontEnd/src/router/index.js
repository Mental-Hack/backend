import { createRouter, createWebHashHistory } from 'vue-router'

import Upload from '../pages/Upload.vue'
import Settings from '../pages/Settings.vue'
import Results from '../pages/Results.vue'
import Navigation from '../pages/Navigation.vue'
import Cows from '../pages/Cows.vue'
import InfoAboutFarm from '../pages/InfoAboutFarm.vue'
import BestPerfomance from '../pages/BestPerfomance.vue'
import Match from '../pages/Match.vue'
import Login from '../pages/Login.vue'
import Control from '../pages/Control.vue'
import Main from '../pages/Main.vue'
import Milk from '../pages/Milk.vue'
import Meat from '../pages/Meat.vue'
import MilkMeat from '../pages/MilkMeat.vue'

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/main',
      name: 'main',
      component: Main,
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/control',
      name: 'control',
      component: Control,
    },
    {
      path: '/',
      name: 'home',
      component: Upload,
    },
    {
      path: '/navigation',
      name: 'navigation',
      component: Navigation
    },
    {
      path: '/cows',
      name: 'cows',
      component: Cows
    },
    {
      path: '/info',
      name: 'info',
      component: InfoAboutFarm
    },
    {
      path: '/settings',
      name: 'settings',
      component: Settings
    },
    {
      path: '/match',
      name: 'match',
      component: Match
    },
    {
      path: '/best-perfomance',
      name: 'best-perfomance',
      component: BestPerfomance
    },
    {
      path: '/evaluate',
      name: 'evaluate',
      component: Results
    },
    {
      path: '/milk',
      name: 'milk',
      component: Milk
    },
    {
      path: '/meat',
      name: 'meat',
      component: Meat
    },
    {
      path: '/correlation',
      name: 'correlation',
      component: MilkMeat
    }
  ],
})

export default router
