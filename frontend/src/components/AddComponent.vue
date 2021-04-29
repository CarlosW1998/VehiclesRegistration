<template>
  <div>
    <form novalidate class="md-layout" @submit.prevent="validateVehicle">
      <md-card class="md-layout-item md-size-100 md-small-size-100">
        <md-card-header>
          <div class="md-title">Veiculo</div>
        </md-card-header>

        <md-card-content>
          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('model')">
                <label for="first-name">Modelo</label>
                <md-input name="model" id="model" v-model="form.model" :disabled="sending" />
                <span class="md-error" v-if="!$v.form.model.required">CAMPO ORBIGATORIO</span>
                <span class="md-error" v-else-if="!$v.form.model.minlength">MÍNIMO DE 3 CARACTERES</span>
                <span class="md-error" v-else-if="!$v.form.model.maxLength">MÁXIMO DE 50 CARACTERES</span>
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('brand')">
                <label for="first-name">Marca</label>
                <md-input name="brand" id="brand" v-model="form.brand" :disabled="sending" />
                <span class="md-error" v-if="!$v.form.brand.required">CAMPO ORBIGATORIO</span>
                <span class="md-error" v-else-if="!$v.form.brand.minlength">MÍNIMO DE 3 CARACTERES</span>
                <span class="md-error" v-else-if="!$v.form.brand.maxLength">MÁXIMO DE 50 CARACTERES</span>
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('price')">
                <label for="age">Preço</label>
                <md-input type="number" id="price" name="price" v-model="form.price" :disabled="sending" />
                <span class="md-error" v-if="!$v.form.price.required">CAMPO ORBIGATORIO</span>
              </md-field>
            </div>
            

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('note')">
                <label for="first-name">Observações</label>
                <md-textarea name="note" id="note" v-model="form.note" :disabled="sending" />
                <span class="md-error" v-if="!$v.form.note.required">CAMPO ORBIGATORIO</span>
                <span class="md-error" v-else-if="!$v.form.note.minlength">MÍNIMO DE 3 CARACTERES</span>
                <span class="md-error" v-else-if="!$v.form.note.maxLength">MÁXIMO DE 500 CARACTERES</span>
                </md-field>
            </div>
        </div>  
        </md-card-content>

        <md-progress-bar md-mode="indeterminate" v-if="sending" />

        <md-card-actions>
          <md-button type="submit" class="md-primary" :disabled="sending">Criar Veículo</md-button>
        </md-card-actions>
      </md-card>

      <md-snackbar :md-active.sync="vehicleSaved">O Veiculo {{ lastVehicle }} {{mensage}} </md-snackbar>
    </form>
  </div>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import axios from 'axios'
  import {
    required,
    minLength,
    maxLength
  } from 'vuelidate/lib/validators'

  export default {
    
    mixins: [validationMixin],
    data: () => ({
      mensage: String,
      form: {
        model: null,
        brand: null,
        price: null,
        note: null,
      },
      vehicleSaved: false,
      sending: false,
      lastVehicle: null
    }),
    validations: {
      form: {
        model: {
          required,
          minLength: minLength(3),
          maxLength: maxLength(50)
        },
        brand: {
          required,
          minLength: minLength(3),
          maxLength: maxLength(50)
        },
        price: {
          required,
        },
        note: {
          required,
          minLength: minLength(3),
          maxLength: maxLength(500)
        },
      }
    },
    methods: {
      getValidationClass (fieldName) {
        const field = this.$v.form[fieldName]

        if (field) {
          return {
            'md-invalid': field.$invalid && field.$dirty
          }
        }
      },
      clearForm () {
        this.$v.$reset()
        this.form.model = null
        this.form.brand = null
        this.form.price = null
        this.form.note = null
      },
      saveVehicle () {
        this.sending = true
        axios.post('http://localhost:8000/api/vehicle/', this.form,
        {crossdomain: true})
        .then(response=>{
          response
          this.lastVehicle = `${this.form.model}`
          this.mensage = 'foi salvo com sucesso!'
          this.vehicleSaved = true
          this.sending = false
          this.clearForm()
        })
        .catch(error=>{
          error
          this.mensage = 'não foi salvo com sucesso'
          this.vehicleSaved = true
          this.sending = false
          
        })
      },
      validateVehicle () {
        this.$v.$touch()

        if (!this.$v.$invalid) {
          this.saveVehicle()
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  .md-progress-bar {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
  }
</style>