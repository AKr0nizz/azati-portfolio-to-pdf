def execute_cleanup_scripts(driver):

    # Remove Header
    driver.run_script("""let removeHeader = () => {
    let header = document.querySelector(".header-wrapper");
    header.parentNode.removeChild(header);
    };
    removeHeader();
    """)

    # Remove Star Rating
    driver.run_script("""let removeStarRating = () => {
    let starRating = document.querySelector(".kk-star-ratings");
    starRating.parentNode.removeChild(starRating);
    };
    removeStarRating();
    """)

    # Remove Site Footer
    driver.run_script("""let removeSiteFooter = () => {
    let siteFooter = document.querySelector(".site-footer");
    siteFooter.parentNode.removeChild(siteFooter);
    };
    removeSiteFooter();
    """)
