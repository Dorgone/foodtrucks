import Route from '@ember/routing/route';

export default Route.extend({
  redirect() {
    this.transitionTo('foodtrucks'); // redirects root url "/" to "/foodtrucks"
  }
});