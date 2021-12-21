<template lang="pug">
v-progress-circular#fakeLoader(
  :value="progress"
  :color="progress === '100' ? '#4CAF50' : 'primary'"
  style="transition: none"
  :size="size"
  :width="width"
)
  b(v-if="progress !== null" style="font-size: 35px") {{ progress + '%' }}
</template>

<script>
import TWEEN from '@tweenjs/tween.js'

export default {
  model: {
    prop: 'finished',
    event: 'update'
  },
  props: {
    duration: {
      type: Number,
      default: () => 1000
    },
    size: {
      type: [String, Number],
      default: () => 200
    },
    width: {
      type: [String, Number],
      default: () => 4
    },
    autoStart: {
      type: Boolean,
      default: () => false
    },
    finished: {
      type: Boolean,
      default: () => false
    }
  },
  data() {
    return {
      progress: 0,
      step: 1
    }
  },
  methods: {
    tween() {
      // Handles updating the tween on each frame.
      const vm = this

      const animate = function (currentTime) {
        TWEEN.update(currentTime)
        requestAnimationFrame(animate)
      }

      new TWEEN.Tween({ tweeningNumber: 0 })
        .to({ tweeningNumber: 100 }, this.duration)
        .onUpdate((myTween) => {
          vm.progress = myTween.tweeningNumber.toFixed(0)
        })
        .onComplete(() => {
          // Make sure to clean up after ourselves.
          // console.log(`finished`)
          vm.$emit('update', true)
        })
        // This actually starts the tween.
        .start()

      animate()
    }
  },
  mounted() {
    this.tween()
    // if (this.autoStart) {
    // }
  }
}
</script>

<style>
div#fakeLoader > svg > circle.v-progress-circular__overlay {
  transition: none !important;
  -webkit-transition: none !important;
}
</style>
