<template>
  <div>
    <section class="section">
      <div class="container is-fluid">
          <h1 class="title has-text-info">
            Тарифы
          </h1>
     <TariffsTable></TariffsTable>
      </div>
    </section>
  </div>
</template>

<script>
import TariffsTable from "@/components/TariffsTable.vue";

export default {

  components: {
    TariffsTable
  },
 
  mounted() {
    document.title = 'Тарифы | DoveCuments'
  },
}
</script>

<style lang="scss" scoped>
</style>
