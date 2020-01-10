let removeSiteFooter = () => {
  let siteFooter = document.querySelector(".site-footer");
  siteFooter.parentNode.removeChild(siteFooter);
};
removeSiteFooter();
