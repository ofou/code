Date.prototype.addGigaseconds = function () {
  var gigasecond = 1000000000;
  return new Date(this.getTime() + gigasecond * 1000);
};

export const gigasecond = (moment) => {
  return moment.addGigaseconds();
};
