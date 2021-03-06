<template>
  <v-form
    ref="form5"
    v-model="valid"
  >
<v-container>
  <v-row class="mt-6 ml-4">
    <span class="subtitle-1">
      Wähle so viele thematische Kategorien aus, wie zu deiner Heimabend-Idee passen. <br>
      <br>
      Wenn du noch eine Kategorie hinzufügen möchtest, kannst du dich
      gerne mit dem Kontaktformular direkt an uns wenden.
    </span>
  </v-row>
  <v-row class="ma-6">
    <v-select
      v-model="data.tags"
      :items="getSideBarTags"
      item-value="id"
      :rules="rules.tags"
      item-text="name"
      deletable-chips
      chips
      dense
      no-data-text="Wähle aus der Liste Probenordnung aus."
      multiple
      outlined
    >
      <template v-slot:selection="{ item, index }">
        <v-chip v-if="index < 3" :color="item.color" small>
          <span>{{ item.name }}</span>
        </v-chip>
        <span
          v-if="index === 3"
          class="grey--text caption"
        >
          (+ ...)
        </span>
      </template>
    </v-select>
  </v-row>

    <v-divider class="my-2"/>
    <v-row class="ma-3" justify="center">
      <v-btn
        class="mr-5"
        @click="prevStep()"
      >
        Zurück
      </v-btn>

      <v-btn
        color="primary"
        @click="nextStep()"
      >
        Weiter
      </v-btn>
    </v-row>
</v-container>
        </v-form>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  data: () => ({
    rules: {
      tags: [
        v => (v && v.length > 0) || 'Mindestens ein Thema ist erforderlich',
      ],
    },
    data: {
      executionTimeRating: 1,
      costsRating: 1,
      isLvlOne: true,
      isLvlTwo: true,
      isLvlThree: true,
    },
    valid: true,
    n: 0,
  }),

  computed: {
    ...mapGetters([
      'tags',
      'tagCategory',
    ]),
    isMobil() {
      return this.$vuetify.breakpoint.mdAndDown;
    },
    tags() {
      return this.$store.getters.tags;
    },
    isCreate() {
      return !this.$route.params.id;
    },
    isUpdate() {
      return !!this.$route.params.id;
    },
    isLargeProject() {
      return this.data.executionTimeRating === 0;
    },
    largeProjectButtomColor() {
      return this.isLargeProject ? 'limegreen' : 'lightgrey';
    },
    largeProjectIconColor() {
      return this.isLargeProject ? 'black' : 'grey';
    },
    isWithoutCosts() {
      return this.data.costsRating === 0;
    },
    withoutCostsButtomColor() {
      return this.isWithoutCosts ? 'limegreen' : 'lightgrey';
    },
    withoutCostsIconColor() {
      return this.isWithoutCosts ? 'red darken-2' : 'grey';
    },
    getClassForTextContentSteps() {
      return this.isMobil ? 'mx-0 px-1' : '';
    },
    getTopBarTagCategories() {
      if (this.tagCategory) {
        return this.tagCategory
          .filter(item => item.is_header);
      }
      return [];
    },
    getSideBarTags() {
      if (this.tags && this.tagCategory) {
        const sideBarTagCategories = this.tagCategory.filter(item => item.is_header === false);
        const sideBarTags = this.filterTagByCategory(sideBarTagCategories[0].id);
        return sideBarTags;
      }
      return [];
    },

  },

  mounted() {
    if (this.$route.params.id) {
      this.data = this.$route.params;
    }
  },

  created() {
    if (this.$route.params.id) {
      this.data = this.$route.params;
    }
  },


  methods: {
    filterTagByCategory(categoryId) {
      return this.tags.filter(item => item.category === categoryId);
    },
    prevStep() {
      this.$emit('prevStep');
    },
    nextStep() {
      if (!this.$refs.form5.validate()) {
        return;
      }
      this.$emit('nextStep');
    },
    getData() {
      return {
        tags: this.data.tags,
      };
    },
    getMandatoryBarTagCategories() {
      if (this.tagCategory) {
        return this.tagCategory
          .filter(item => item.is_mandatory);
      }
      return [];
    },
    getCategoryIdByTagId(categoryId) {
      if (this.categoryId) {
        return this.tags.filter(tag => tag.id === categoryId)[0];
      }
      return [];
    },
    getRulesByCategory(category) {
      let returnValue = this.rules.tags;
      if (!category.is_mandatory) {
        return [];
      }

      if (this.data && this.data.tags) {
        const activeTags = this.tags.filter(tag => this.data.tags.includes(tag.id));
        const containsCategoryId = activeTags.filter(tag => tag.category === category.id); // eslint-disable-line
        if (containsCategoryId.length) {
          returnValue = [];
        }
      }
      return returnValue;
    },
  },
};
</script>
