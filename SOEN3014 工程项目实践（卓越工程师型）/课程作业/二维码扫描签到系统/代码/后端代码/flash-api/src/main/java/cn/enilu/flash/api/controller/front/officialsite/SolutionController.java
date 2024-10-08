package cn.enilu.flash.api.controller.front.officialsite;

import cn.enilu.flash.api.controller.BaseController;
import cn.enilu.flash.bean.entity.cms.Article;
import cn.enilu.flash.bean.enumeration.cms.BannerTypeEnum;
import cn.enilu.flash.bean.enumeration.cms.ChannelEnum;
import cn.enilu.flash.bean.vo.front.Rets;
import cn.enilu.flash.bean.vo.offcialsite.BannerVo;
import cn.enilu.flash.bean.vo.offcialsite.Solution;
import cn.enilu.flash.service.cms.ArticleService;
import cn.enilu.flash.service.cms.BannerService;
import cn.enilu.flash.utils.Maps;
import cn.enilu.flash.utils.factory.Page;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/offcialsite/solution")
public class SolutionController extends BaseController {

    private final BannerService bannerService;

    private final ArticleService articleService;

    public SolutionController(BannerService bannerService, ArticleService articleService) {
        this.bannerService = bannerService;
        this.articleService = articleService;
    }

    @GetMapping
    public Object index() {
        Map<String, Object> dataMap = Maps.newHashMap();

        BannerVo banner = bannerService.queryBanner(BannerTypeEnum.SOLUTION.getValue());
        dataMap.put("banner", banner);

        List<Solution> solutions = new ArrayList<>();
        Page<Article> articlePage = articleService.query(1, 10, ChannelEnum.SOLUTION.getId());
        for (Article article : articlePage.getRecords()) {
            solutions.add(new Solution(article.getId(), article.getTitle(), article.getImg()));
        }
        dataMap.put("solutionList", solutions);

        Map map = Maps.newHashMap("data", dataMap);
        return Rets.success(map);
    }

}
